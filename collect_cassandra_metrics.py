from cassandra.cluster import Cluster
import psutil

def collect_cassandra_metrics():
    # Connect to the Cassandra cluster
    cluster = Cluster(['localhost'])  
    session = cluster.connect()
    # Retrieve performance-related metrics
    metrics = {}
    # Node CPU and memory usage
    cpu_percent = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    metrics['CPU Usage (%)'] = cpu_percent
    metrics['Memory Usage (%)'] = memory_usage
    # Read and write latencies
    read_latency = session.execute("SELECT mean_read_latency FROM system.local").one().mean_read_latency
    write_latency = session.execute("SELECT mean_write_latency FROM system.local").one().mean_write_latency
    metrics['Read Latency (ms)'] = read_latency
    metrics['Write Latency (ms)'] = write_latency
    # Number of pending compactions
    compaction_count = session.execute("SELECT pending_compactions FROM system.local").one().pending_compactions
    metrics['Pending Compactions'] = compaction_count
    # Number of active connections
    active_connections = session.execute("SELECT active_connections FROM system.local").one().active_connections
    metrics['Active Connections'] = active_connections

    # Storage space utilization
    storage_metrics = session.execute("SELECT data_center, rack, keyspace_name, table_name, total_space_used FROM system.size_estimates")
    for storage_metric in storage_metrics:
        key = f"{storage_metric.data_center}.{storage_metric.rack}.{storage_metric.keyspace_name}.{storage_metric.table_name}"
        metrics[key] = storage_metric.total_space_used
    # Print collected metrics
    for key, value in metrics.items():
        print(f"{key}: {value}")
    # Close the connection
    session.shutdown()
    cluster.shutdown()

# Call the function to collect metrics
collect_cassandra_metrics()
