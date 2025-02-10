export async function Status() {
  let cluster_data = await fetch('http://127.0.0.1:8000/api/cluster/'); // FIX: don't hard-code this
  let node_data = await fetch('http://127.0.0.1:8001/api/v1/nodes'); // FIX: don't hard-code this
  let cluster = await cluster_data.json();
  let nodes = await node_data.json();

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
        <br></br>
        Nodes online:
        <ul>
          {nodes.items.map((c) => (
            <li key={c.metadata.name}>{c.metadata.name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
