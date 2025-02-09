export async function Status() {
  let data = await fetch('http://127.0.0.1:8000/api/cluster/'); // FIX: don't hard-code this
  let cluster = await data.json();

  return (
    <div>
      <h1 className="text-xl md:text-3xl">Status</h1>
      <div className="py-4">
        <ul>
          {cluster.map((c) => (
            <li key={c.id}>
              {c.name}: {c.machine_type} – {c.cpus} CPUs, {c.memory} GB RAM
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
