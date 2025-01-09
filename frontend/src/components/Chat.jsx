import React, { useState } from 'react';
import { ChevronLeft } from 'lucide-react';

const Header = () => (
  <div className="header">
    <button className="back-button">
      <ChevronLeft size={20} color="#000"/>
    </button>
    <div className="logo">
      <svg viewBox="0 0 24 24" width="24" height="24">
        <circle cx="12" cy="12" r="10" fill="#0066B3"/>
        <circle cx="12" cy="12" r="3" fill="white"/>
      </svg>
    </div>
  </div>
);

const Message = ({ text, isOutgoing }) => (
  <div className={`message ${isOutgoing ? 'outgoing' : 'incoming'}`}>
    <div className="message-bubble">
      {text}
    </div>
  </div>
);

const Chat = () => {
  const [messages] = useState([
    {
      id: 1,
      text: "Eno, tell me a joke",
      isOutgoing: true
    },
    {
      id: 2,
      text: 'Q: When does it rain money?\n\nA: When there\'s a "change" in the weather.',
      isOutgoing: false
    }
  ]);

  return (
    <div className="chat-container">
      <Header />
      <div className="messages-container">
        {messages.map((message) => (
          <Message
            key={message.id}
            text={message.text}
            isOutgoing={message.isOutgoing}
          />
        ))}
      </div>
    </div>
  );
};

export default Chat;