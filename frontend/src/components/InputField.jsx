import React from 'react';
import '../styles/Pages.css';

function InputField({ type, value, onChange, placeholder, required = true }) {
  return (
    <input
      type={type}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      required={required}
      className="input-field"
    />
  );
}

export default InputField;
