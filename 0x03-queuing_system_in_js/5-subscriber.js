import redis from 'redis';

const redis_url = process.env.REDIS_URL ?? 'redis://localhost:6379'
const client = redis.createClient(redis_url);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  console.log('Message received on channel ' + channel + ': ' + message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
