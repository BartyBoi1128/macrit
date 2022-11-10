import React, { useState } from 'react';
import "../navbar.css";

function Navbar() {
    const [active, setActive] = useState("nav_menu");
    const [toggleIcon, setToggleIcon] = useState("nav_toggle");
    const navSwitch = () => {
        active === "nav_menu" ? setActive("nav_menu nav_active") : setActive("nav_menu");
        toggleIcon === "nav_toggle" ? setToggleIcon("nav_toggle toggle") : setToggleIcon("nav_toggle");
    }
    return (
        <nav className="nav">
            <a href="#" className="brand">macrit</a>
            <ul className={active}>
                <li className="nav_item">
                    <a href="#" className="nav_link">
                        Recipes
                        </a>
                </li>
                <li className="nav_item">
                    <a href="#" className="nav_link">
                        Macros
                    </a>
                </li>
                <li className="nav_item">
                    <a href="#" className="nav_link">
                        Profile
                    </a>
                </li>
                <li className="nav_item">
                    <a href="/settings" className="nav_link">
                        Settings
                    </a>
                </li>
            </ul>
            <div onClick = {navSwitch} className={toggleIcon}>
                <div className="line1"></div>
                <div className="line2"></div>
                <div className="line3"></div>
            </div>
        </nav>
    );
}

export default Navbar;