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
    <div className="w-full max-w-xs">
      <form className="bg-black shadow-md rounded px-8 pt-6 pb-8 mb-4" onSubmit={handleSubmit}>
        <div className="mb-4">
          <label>
            Event name
            <input
              type="text"
              name="name"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Data 8"
              value={formData.name}
              onChange={handleChange}
            />
          </label>
        </div>
        <div className="mb-4">
          <label>
            Event description
            <textarea
              name="description"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="This workshop is for the class of 2024/25, Semester 2."
              value={formData.description}
              onChange={handleChange}
            ></textarea>
          </label>
        </div>
        <div className="mb-4">
          <input
            name="start_time"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Event start"
            type="datetime-local"
            value={formData.start_time}
            onChange={handleChange}
          />
        </div>
        <div className="mb-4">
          <input
            name="end_time"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            placeholder="Event end"
            type="datetime-local"
            value={formData.end_time}
            onChange={handleChange}
          />
        </div>
        <div className="mb-4">
          <label>
            Number of users
            <input
              name="num_users"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              type="number"
              value={formData.num_users}
              onChange={handleChange}
            />
          </label>
        </div>
        <div className="mb-4">
          <label>
            CPUs per user
            <input
              name="cpus_per_user"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              type="number"
              value={formData.cpus_per_user}
              onChange={handleChange}
            />
          </label>
        </div>
        <div className="mb-4">
          <label>
            RAM (GB) per user
            <input
              name="memory_per_user"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              type="number"
              value={formData.memory_per_user}
              onChange={handleChange}
            />
          </label>
        </div>
        <div className="mb-4">
          <Button type="submit">Submit</Button>
        </div>
      </form>
    </div>
  );
};

export default FormComponent;
