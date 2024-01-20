'use client'
import React from "react";
import Header from "../components/header";
import { CldImage, CldVideoPlayer } from "next-cloudinary";
import axios from "axios";
export default function Posts({info}:{info:any})
{
    return(<>
        <Header />
         Feed <br/>
         <button className='yellow' onClick={()=>{
          window.location.href = "/posts/newpost"
         }}> New Post</button>
      
      
      
      
      
        {info.map((item: any)=>(
        <div key={item.id} className = "post-container">
         <div key={item.id} >
           <br/>
           
          <div>
          <div className="post-content">
          {item.format == "jpg" ?(<CldImage
           id={item.public_id}
           width="200"
           height="200"
           src = {item.public_id}
           sizes="100vw"
      
           alt="Description of my image"
           />): (<CldVideoPlayer 
            id={item.public_id}
            width="200"
            height="200"
            transformation={{
              crop:"fill", 
              
      
            }}
            src={item.public_id}
            
                />)} </div></div>
                <div className='post-caption'>
           Caption : {item.caption} </div>
           <br/>
          <button  className= "delete-button" onClick ={async ()=>{
            const res = await axios.delete(`http://localhost:8000/post/${item.id}/`);
            const info = res.data;
            console.log(info);
            window.location.reload()
          
          }} > Delete </button>
          <br/>
          <br/>
          <button  className = "edit-button" onClick = {async()=>
          {
            window.location.href = `/posts/editpost/${item.id}`
      
          }}> Edit</button>
          </div>
          </div>
      
      
        ))} 
        </>)
}