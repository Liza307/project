import { Route, Routes } from "react-router-dom";
import "./App.css";
import Header from "./components/Header/Header";
import Catalogs from "./pages/Catalogs/Catalogs";
import Company from "./pages/Company/Company";
import Projects from "./pages/Projects/Projects";
import Burger from "./pages/Burger/Burger";
import SideBar from "./components/SideBar/SideBar";
import Profile from "./pages/Profile/Profile";

function App() {
  return (
    <div className="App">
      <Header></Header>
      <main className="main">
        <SideBar></SideBar>
        <Routes>
          <Route exact path="/company" element={<Company></Company>}></Route>
          <Route exact path="/projects" element={<Projects></Projects>}></Route>
          <Route exact path="/catalogs" element={<Catalogs></Catalogs>}></Route>
          <Route exact path="/profile" element={<Profile></Profile>}></Route>
          <Route exact path="/burger" element={<Burger></Burger>}></Route>
        </Routes>
      </main>
    </div>
  );
}

export default App;
