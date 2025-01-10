import React, { useState } from 'react';
import { ChevronUp, ChevronDown, Bell, HelpCircle, User } from 'lucide-react';

const FinancialCard = ({ title, subtitle, children, defaultExpanded = true }) => {
  const [isExpanded, setIsExpanded] = useState(defaultExpanded);
  
  return (
    <div className="bg-white rounded-lg shadow-sm mb-4 p-4">
      <div 
        className="flex justify-between items-center cursor-pointer" 
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <div>
          <h2 className="text-lg font-semibold text-gray-800">{title}</h2>
          <p className="text-sm text-gray-500">{subtitle}</p>
        </div>
        {isExpanded ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
      </div>
      {isExpanded && (
        <div className="mt-4 space-y-3">
          {children}
        </div>
      )}
    </div>
  );
};

const AccountItem = ({ title, subtitle }) => (
  <div className="py-2">
    <div className="text-gray-800">{title}</div>
    <div className="text-sm text-gray-500">{subtitle}</div>
  </div>
);

const DashboardLayout = ({ children }) => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center space-x-8">
              <div className="text-2xl font-bold text-blue-500">SoFi</div>
              <nav className="space-x-6">
                <a href="#" className="text-blue-500 border-b-2 border-blue-500 pb-4">Home</a>
                <a href="#" className="text-gray-500">Banking</a>
                <a href="#" className="text-gray-500">Credit Card</a>
                <a href="#" className="text-gray-500">Invest</a>
              </nav>
            </div>
            <div className="flex items-center space-x-4">
              <button className="p-2">
                <HelpCircle size={20} />
              </button>
              <button className="p-2">
                <Bell size={20} />
              </button>
              <button className="flex items-center space-x-2 bg-blue-500 text-white px-3 py-1 rounded">
                <User size={16} />
                <span>Nathan</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 py-6">
        <h1 className="text-3xl font-semibold text-gray-800 mb-6">Hi Nathan</h1>
        
        <div className="flex gap-6">
          {/* Left Column - Financial Information */}
          <div className="w-1/2">
            <FinancialCard 
              title="Banking" 
              subtitle="0 transactions today"
            >
              <AccountItem title="Checking" subtitle="0 transactions today" />
              <AccountItem title="Savings" subtitle="Saved this month" />
            </FinancialCard>

            <FinancialCard 
              title="Relay Insights" 
              subtitle="4 SoFi accounts"
            >
              <AccountItem title="Cash" subtitle="2 SoFi accounts" />
              <AccountItem title="Investments" subtitle="2 SoFi accounts" />
              <AccountItem title="Credit cards" subtitle="0 accounts" />
              <div className="text-blue-500 text-sm mt-2">View all (4)</div>
            </FinancialCard>

            <FinancialCard 
              title="Personal Loan" 
              subtitle=""
              defaultExpanded={false}
            />
          </div>

          {/* Right Column - Chat Interface */}
          <div className="w-1/2">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardLayout;