import { Heading, Input } from '@chakra-ui/react';

function Home() {
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
          fontFamily: 'inter',
          fontWeight: 700,
          fontSize: '2rem',
          marginTop: '1rem',
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
        placeholder="Enter your symptoms"
      ></Input>

      <div
        style={{
          marginTop: '2rem',
          gap: '1rem',
          display: 'flex',
          justifyContent: 'space-between',
        }}
      >
        <a href="/home">
          <u>Home</u>
        </a>
        <a href="/calendar">Calendar</a>
      </div>

      <div>
        <Heading
          style={{
            fontSize: '1.5rem',
            padding: '2rem 0rem',
            color: '#535353',
            fontWeight: 600,
            textAlign: 'center',
          }}
        >
          Common Symtptoms Currently 🌧️
        </Heading>

        <div style={cardStyle}>
          <h3 style={cardStyleH3}>Light Fever</h3>
          <p style={{ color: '#888' }}>
            The medical community generally defines a fever as a body temperature above 100.4
            degrees Fahrenheit. A body temp between 100.4 and 102.2 degree is usually considered a
            low-grade fever. “If the temperature is not high, it doesn&apos;t necessarily need to be
            treated with medication,” Dr. Joseph
          </p>
        </div>

        <div style={cardStyle}>
          <h3 style={cardStyleH3}>Stuffy Nose</h3>
          <p style={{ color: '#888' }}>
            Nasal congestion can be caused by anything that irritates or inflames the nasal tissues.
            Infections — such as colds, flu or sinusitis — and allergies are frequent causes of
            nasal congestion and runny nose. Sometimes a congested and runny nose can be caused by
            irritants such as tobacco smoke and car exhaust.
          </p>
        </div>

        <div style={cardStyle}>
          <h3 style={cardStyleH3}>Coughing</h3>
          <p style={{ color: '#888' }}>
            While an occasional cough is normal, a cough that persists may be a sign of a medical
            problem. A cough is considered &quot;acute&quot; if it lasts less than three weeks. It
            is considered &quot;chronic&quot; if it lasts longer than eight weeks (four weeks in
            children).
          </p>
        </div>
      </div>
    </div>
  );
}

export default Home;

const cardStyle = {
  padding: '1.5rem',
  border: '2px solid #E2E8F0',
  borderRadius: '2rem',
  width: '490px',
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  margin: '1rem',
  minHeight: '200px',
};

const cardStyleH3 = {
  textAlign: 'left',
  width: '100%',
  fontSize: '1.2rem',
  fontWeight: 500,
  marginBottom: '7px',
};
