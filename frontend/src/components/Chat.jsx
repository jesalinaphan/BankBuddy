import React, { useState } from 'react';
import { ChevronLeft, Send } from 'lucide-react';

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

const MessageInput = ({ onSend }) => {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      onSend(message);
      setMessage('');
    }
  };

  return (
    <form className="message-input-container" onSubmit={handleSubmit}>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message..."
        className="message-input"
      />
      <button type="submit" className="send-button" disabled={!message.trim()}>
        <Send size={20} color={message.trim() ? '#0066B3' : '#999'} />
      </button>
    </form>
  );
};

const Chat = () => {
  const [messages, setMessages] = useState([
    {
      id: 2,
      text: 'Hi there! How can I help you today?',
      isOutgoing: false
    }
  ]);

  const handleSendMessage = (text) => {
    const newUserMessage = {
      id: messages.length + 1,
      text,
      isOutgoing: true
    };
    
    const botResponse = {
      id: messages.length + 2,
      text: "Thanks for your message! This is a dummy response.",
      isOutgoing: false
    };

    setMessages([...messages, newUserMessage, botResponse]);
  };

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
      <MessageInput onSend={handleSendMessage} />
    </div>
  );
};

export default Chat;