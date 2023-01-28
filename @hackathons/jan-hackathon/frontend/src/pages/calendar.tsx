import 'react-calendar/dist/Calendar.css';

import { Heading, Input } from '@chakra-ui/react';
import { useState } from 'react';
import Calendar from 'react-calendar';

function CalendarFC() {
  const [date, onChange] = useState(new Date());
  return (
    <div
      style={{
        padding: '1.5rem',
        border: '2px solid #E2E8F0',
        borderRadius: '2rem',
        width: '600px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        margin: '1rem',
        minHeight: '96vh',
        background: '#fefefe',
        boxShadow: '4px 4px 6px 0px #dedede',
      }}
    >
      <Heading
        style={{
          fontWeight: 700,
          fontSize: '2rem',
        }}
      >
        Symptom Tracker
      </Heading>

      <Input
        style={{
          marginTop: '2rem',
          textAlign: 'center',
          maxWidth: '500px',
          border: '2px solid #dedede',
          borderRadius: '0.8rem',
        }}
        placeholder="Search symptoms in calander"
      ></Input>

      <div
        style={{
          marginTop: '2rem',
          gap: '1rem',
          display: 'flex',
          justifyContent: 'space-between',
        }}
      >
        <a href="/home">Home</a>
        <a href="/calendar">
          <u>Calendar</u>
        </a>
      </div>

      <br />
      <Calendar onChange={onChange} value={date} />
    </div>
  );
}

export default CalendarFC;
