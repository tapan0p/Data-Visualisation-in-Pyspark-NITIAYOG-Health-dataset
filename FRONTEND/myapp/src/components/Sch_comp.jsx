import React, { useEffect, useState } from 'react';

const Sch_comp = () => {
  const [schema, setSchema] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/schema')
      .then(response => response.json())
      .then(data => setSchema(data.schema))
      .catch(error => console.error('Error fetching schema:', error));
  }, []);

  return (
    <div>
      <h1>PySpark DataFrame Schema</h1>
      {schema && <pre>{JSON.stringify(schema, null, 2)}</pre>}
    </div>
  );
};

export default Sch_comp;
