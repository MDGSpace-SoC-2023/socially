'use client'
import { CldVideoPlayer } from "next-cloudinary";
import React from "react";
export default function Home()
{
    return(<>
    <header>
  <h1>Your Doodle Header</h1>
  <div className="doodle-container">
    <div className="doodle"></div>
    <div className="doodle"></div>
    <div className="doodle"></div>
  </div>
</header>
    
    </>
    )
}