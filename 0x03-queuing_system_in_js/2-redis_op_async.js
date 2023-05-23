import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
