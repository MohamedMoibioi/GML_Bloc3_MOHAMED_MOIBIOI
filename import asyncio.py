import asyncio 
import aiohttp 
import sqlite3 
import logging 
 
MAX_BUFFER_SIZE = 1000  # Limitation stricte pour préserver la RAM 
 
class TelemetryManager: 
    def __init__(self, db_path='telemetry.db'): 
        self.conn = sqlite3.connect(db_path) 
        self.create_table() 
        self.queue = asyncio.Queue(maxsize=MAX_BUFFER_SIZE) 
 
    def create_table(self): 
        self.conn.execute('CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY, 
data TEXT)') 
 
    async def produce_sensor_data(self): 
        while True: 
            val = {'x': 12, 'y': -3.0} 
            if val['y'] < -2.5: 
                if self.queue.full(): 
                    _ = await self.queue.get()  # Nettoyage FIFO si saturation 
                await self.queue.put(val) 
            await asyncio.sleep(0.1) 
 
    async def consume_and_send_alerts(self): 
        async with aiohttp.ClientSession() as session: 
            while True: 
                val = await self.queue.get() 
                try: 
                    async with session.post('https://api.gml.com/v1/alert', 
                                            json=val, 
                                            headers={'Authorization': 'Bearer 
TOKEN_SECURE'}, 
                                            timeout=aiohttp.ClientTimeout(total=3)) as 
resp: 
                        if resp.status != 200: 
                            self.store_local_backup(val) 
                except Exception: 
                    self.store_local_backup(val) 
                self.queue.task_done() 
self.conn.commit() 
def store_local_backup(self, val): 
self.conn.execute('INSERT INTO alerts (data) VALUES (?)', (str(val),)) 