import { NavLink } from "react-router-dom";
import "./Header.css";

function Header() {
  return (
    <header className="header">
      <div className="header__container">
        <h1 className="header__title">ГИД Структура</h1>
        <div className="header__user-block">
          <NavLink className="header__notifications"  to='/notifications'></NavLink>
          <div className="header__user-info">
            <button className="header__user-logo"></button>
            <p className="header__user-name">Кирилл Егоров</p>
          </div>
          <NavLink className="header__logout" to="/login"></NavLink>
        </div>
      </div>
    </header>
  );
}

export default Header;
