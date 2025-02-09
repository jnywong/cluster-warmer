'use client';

import React, { useState } from 'react';
import { Button } from '../button';
import axios from 'axios';

const FormComponent = () => {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    start_time: '',
    end_time: '',
    num_users: '',
    cpus_per_user: '',
    memory_per_user: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/events/', formData);
      console.log('Form data submitted successfully:', response.data);
      // You can add additional logic here, such as displaying a success message
    } catch (error) {
      console.error('Error submitting form data:', error);
      // You can add error handling logic here, such as displaying an error message
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        placeholder="Enter your name"
        value={formData.name}
        onChange={handleChange}
      />
      <textarea
        name="description"
        placeholder="Optional: Description"
        value={formData.description}
        onChange={handleChange}
      ></textarea>
      <input
        name="start_time"
        placeholder="Event start"
        type="datetime-local"
        value={formData.start_time}
        onChange={handleChange}
      />
      <input
        name="end_time"
        placeholder="Event end"
        type="datetime-local"
        value={formData.end_time}
        onChange={handleChange}
      />
      <input name="num_users" type="number" value={formData.num_users} onChange={handleChange} />
      <input
        name="cpus_per_user"
        type="number"
        value={formData.cpus_per_user}
        onChange={handleChange}
      />
      <input
        name="memory_per_user"
        type="number"
        value={formData.memory_per_user}
        onChange={handleChange}
      />
      <Button type="submit">Submit</Button>
    </form>
  );
};

export default FormComponent;
