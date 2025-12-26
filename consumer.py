"""
WebSocket consumer for multiplayer game
"""
import json
import random
from channels.generic.websocket import AsyncWebsocketConsumer

class GameConsumer(AsyncWebsocketConsumer):
    players = {}
    world_blocks = {}
    world_seed = random.randint(0, 999999999)  # Shared world seed
    
    async def connect(self):
        self.room_name = 'game'
        self.room_group_name = 'game_room'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send player ID and world seed
        await self.send(text_data=json.dumps({
            'type': 'player_id',
            'id': self.channel_name,
            'worldSeed': GameConsumer.world_seed
        }))
        
        # Add player
        GameConsumer.players[self.channel_name] = {
            'id': self.channel_name,
            'x': 0,
            'y': 70,
            'z': 0,
            'rotationY': 0
        }
        
        # Send existing players
        await self.send(text_data=json.dumps({
            'type': 'currentPlayers',
            'players': GameConsumer.players
        }))
        
        # Send existing blocks to new player
        await self.send(text_data=json.dumps({
            'type': 'existingBlocks',
            'blocks': GameConsumer.world_blocks
        }))
        
        # Notify others
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'player_joined',
                'player': GameConsumer.players[self.channel_name]
            }
        )
    
    async def disconnect(self, close_code):
        # Remove player
        if self.channel_name in GameConsumer.players:
            del GameConsumer.players[self.channel_name]
        
        # Notify others
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'player_left',
                'id': self.channel_name
            }
        )
        
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        msg_type = data.get('type')
        
        if msg_type == 'playerMovement':
            # Update player position
            if self.channel_name in GameConsumer.players:
                GameConsumer.players[self.channel_name].update({
                    'x': data['x'],
                    'y': data['y'],
                    'z': data['z'],
                    'rotationY': data['rotationY']
                })
            
            # Broadcast to others
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'player_moved',
                    'id': self.channel_name,
                    'x': data['x'],
                    'y': data['y'],
                    'z': data['z'],
                    'rotationY': data['rotationY']
                }
            )
        
        elif msg_type == 'blockPlaced':
            key = f"{data['x']},{data['y']},{data['z']}"
            GameConsumer.world_blocks[key] = data['blockType']
            
            # Broadcast to all
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'block_placed',
                    'x': data['x'],
                    'y': data['y'],
                    'z': data['z'],
                    'blockType': data['blockType'],
                    'senderId': data.get('senderId')
                }
            )
        
        elif msg_type == 'blockBroken':
            key = f"{data['x']},{data['y']},{data['z']}"
            if key in GameConsumer.world_blocks:
                del GameConsumer.world_blocks[key]
            
            # Broadcast to all
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'block_broken',
                    'x': data['x'],
                    'y': data['y'],
                    'z': data['z'],
                    'senderId': data.get('senderId')
                }
            )
    
    # Group message handlers
    async def player_joined(self, event):
        if event['player']['id'] != self.channel_name:
            await self.send(text_data=json.dumps({
                'type': 'playerJoined',
                'player': event['player']
            }))
    
    async def player_left(self, event):
        if event['id'] != self.channel_name:
            await self.send(text_data=json.dumps({
                'type': 'playerLeft',
                'id': event['id']
            }))
    
    async def player_moved(self, event):
        if event['id'] != self.channel_name:
            await self.send(text_data=json.dumps({
                'type': 'playerMoved',
                'id': event['id'],
                'x': event['x'],
                'y': event['y'],
                'z': event['z'],
                'rotationY': event['rotationY']
            }))
    
    async def block_placed(self, event):
        if event.get('senderId') != self.channel_name:
            await self.send(text_data=json.dumps({
                'type': 'blockPlaced',
                'x': event['x'],
                'y': event['y'],
                'z': event['z'],
                'blockType': event['blockType'],
                'senderId': event.get('senderId')
            }))
    
    async def block_broken(self, event):
        if event.get('senderId') != self.channel_name:
            await self.send(text_data=json.dumps({
                'type': 'blockBroken',
                'x': event['x'],
                'y': event['y'],
                'z': event['z'],
                'senderId': event.get('senderId')
            }))
