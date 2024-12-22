from influxdb_client import InfluxDBClient

InfluxDBClient client = InfluxDBClient(url="http://localhost:8086", token="your-token", org="your-org")
query_api query_api = client.query_api() 
write_api = client.write_api()