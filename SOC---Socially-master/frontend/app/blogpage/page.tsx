'use client'
import React from "react";
import axios from "axios";
import Header from "../components/header";
export default async function Blogpage()
{
    const response =  await axios.get("http://localhost:8000/blogpage/");
    const info = response.data;
    return (<>
    <Header />
    
    <div>
      <h1>BLOG PAGE</h1>
      <button className="yellow" onClick={()=>
      {
        window.location.href = "/blogpage/newblog"
      }}> Create a new blog </button>
      
        {info.map((item:any) => (
          <li key={item.id}>
          <div>
           Title :-  {item.title} <br/>
           Type :-  {item.type} <br/>
           Content :- {item.content} <br/>
          <button className="delete-button" onClick={async () => 
          {
            
            const response = await axios.delete(`http://localhost:8000/blog/${item.id}/`)
            console.log(response.data);
            window.location.reload();


          }}> Delete </button>     
           
           
           
           
           
           
           <button  className = "edit-button"onClick = {()=>
          {
            window.location.href = `/blogpage/editblog/${item.id}/`;


          }}>Edit</button>
           <br/> <br/>
            
            
            </div>
            </li>
         
        ))}
      
    </div>
  
    </>)


}
