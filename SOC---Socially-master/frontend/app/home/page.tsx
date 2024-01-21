'use client'
import { CldVideoPlayer } from "next-cloudinary";
import React from "react";
export default function Home()
{
    return(<>
    <header>
  <h1></h1>
  <div className="doodle-container">
    <div className="doodle"></div>
    <div className="doodle"></div>
    <div className="doodle"></div>
    <button onClick={()=>window.location.href="/home/login"}>Login </button> 

    <br/>


    <button onClick={()=>window.location.href="/home/register"}> Register </button>


  </div>
</header>
    
    </>
    )
}