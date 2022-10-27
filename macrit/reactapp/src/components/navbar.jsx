import React from 'react';
import "../navbar.css";

function Navbar(props) {
    return (
        <nav className="nav">
            <a href="#" className="brand">macrit</a>
            <ul className="nav_menu">
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
                        Settings
                    </a>
                </li>
            </ul>
            <div className="nav_toggle">
                <div className="line1"></div>
                <div className="line2"></div>
                <div className="line3"></div>
            </div>
        </nav>
    );
}

export default Navbar;