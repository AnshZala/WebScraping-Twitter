import fetch from 'node-fetch';
import { HttpsProxyAgent } from 'https-proxy-agent';

// Replace with your ProxyMesh credentials and server
const proxyUrl = 'http://Anshzala12cloud:Anshzala12cloud@us-ca.proxymesh.com:31280';

async function testProxy() {
  const agent = new HttpsProxyAgent(proxyUrl);
  
  try {
    const response = await fetch('https://api.ipify.org?format=json', { agent });
    const data = await response.json();
    
    console.log('Connection successful!');
    console.log('Your IP address through the proxy:', data.ip);
    
    // Test if the IP changed
    const directResponse = await fetch('https://api.ipify.org?format=json');
    const directData = await directResponse.json();
    
    if (data.ip !== directData.ip) {
      console.log('Proxy is working correctly. Your IP address has changed.');
    } else {
      console.log('Warning: Proxy may not be working. IP address did not change.');
    }
  } catch (error) {
    console.error('Error connecting to proxy:', error.message);
  }
}

testProxy();