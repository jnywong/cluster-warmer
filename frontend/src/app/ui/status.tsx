function ResultList(result) {
  const parsedResult = JSON.parse(result.result);

  return (
    <ul>
      {Object.entries(parsedResult).map(([key, value]) => (
        <li key={key}>
          🔥 {key}: at least {value} nodes
        </li>
      ))}
    </ul>
  );
}

export async function Status() {
  let cluster_data = await fetch('http://127.0.0.1:8000/api/cluster/'); // FIX: don't hard-code this
  let node_data = await fetch('http://127.0.0.1:8001/api/v1/nodes');
  let nodepool_data = await fetch('http://127.0.0.1:8000/api/nodepool');
  let cluster = await cluster_data.json();
  let nodes = await node_data.json();
  let nodepool = await nodepool_data.json();

  const nodepool_last = nodepool.reduce((latest, task) => {
    return new Date(task.date_created) > new Date(latest.date_created) ? task : latest;
  }, nodepool[0]);

  const filtered = Object.entries(JSON.parse(nodepool_last.result)).filter(([key]) =>
    key.includes('n2'),
  );

  console.log(filtered[0][1]);

  return (
    <div>
      <h1 className="text-3xl">Status</h1>
      <div className="py-4">
        <ul>
          {cluster.map((c) => (
            <li key={c.id}>
              {c.name}: {c.machine_type} ({c.cpus} CPUs, {c.memory} GB RAM) 🟢{' '}
              {nodes.items.filter((item) => item.metadata.name.includes(c.name)).length} online
            </li>
          ))}
        </ul>
        {/* <br></br>
        Nodes online:
        <ul>
          {nodes.items.map((c) => (
            <li key={c.metadata.name}>{c.metadata.name}</li>
          ))}
        </ul> */}
        <br></br>
        Node pool size configuration:
        <ResultList result={nodepool_last.result} />
      </div>
    </div>
  );
}
