import React, { useState, useEffect } from "https://cdn.skypack.dev/react@17.0.1";
import ReactDOM from "https://cdn.skypack.dev/react-dom@17.0.1";

const App = () => {

    // Add and Remove Class on scroll
    const [scrolltopdata, setscrolltopdata] = useState('');

    useEffect(() => {
        window.addEventListener('scroll', () => {
            if (window.scrollY < 15) {
                setscrolltopdata('');
            } else {
                setscrolltopdata('scrolled');
            }
        });
    }, [])

    return ( <
        React.Fragment >
        <
        div className = { `header-wrapper ${scrolltopdata}` } >
        <
        div className = "container-fluid p-0" >
        <
        div className = "header-part" >
        Scroll Up / Down to see it in Action <
        /div> <
        /div> <
        /div> <
        div className = "section-height" > < /div> <
        /React.Fragment>
    );
}


ReactDOM.render( < App / > , document.getElementById("root"));