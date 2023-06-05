# cassandra_collect_metrics

Question::

Write a tool that will connect to a Cassandra cluster and collect performance-related metrics.
The metrics to collect should include, but not be limited to:
* Node CPU and memory usage
* Read and write latencies
* Number of pending compactions
* Number of active connections
* Storage space utilization
<br>
The output should be displayed on the command-line in key-value type of format
You are not limited to any specific languages or tools to complete this task.
<br>
<br>
Solution::
<br> collect_cassandra_metrics.py <br>
The python code when executed, collect_cassandra_metrics.py will connect to the Cassandra cluster, retrieve the metrics, and print them in a key-value format on the command-line.
