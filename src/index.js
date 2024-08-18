import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter } from "react-router-dom";
import { ConfigProvider } from "antd";
import ruRU from 'antd/lib/locale/ru_RU'

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <ConfigProvider locale={ruRU}>
        <App />
      </ConfigProvider>
    </BrowserRouter>
  </React.StrictMode>
);

reportWebVitals();
