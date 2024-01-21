'use client'
import axios from "axios";
import React, { use, useState } from "react";
export default function Page({onAdd}:{onAdd:any})
{
const[valid, setValid] = useState(false);
const [meme, setMeme] = useState({
        url:'',
        title:'',
        user:1,
    })
        
   return (<>
    ASK A QUESTION : 
        <br/>
        <button type ="button"onClick={async ()=>{
           const response = await axios.get("https://meme-api.com/gimme/1");
    
           const url = response.data.memes[0].url;
           const title = response.data.memes[0].title;
            console.log(url);
            console.log(title);
            setValid(true)
            setMeme((prevData) => ({
                ...prevData,
                url:url,
                title:title,
                
            }))
           
            

            console.log(meme);

        }}> Show me a meme </button>
       <br/>
        
    {valid?(<><img src={meme['url']} height={300} width={300}/> <br/> <h1>{meme.title}</h1></>):(<p></p>)}
       
       
       {!valid?(<p>  </p>):(<button className="delete-button" onClick={()=>onAdd(meme,valid)}> Add meme</button>)}
       
       </>);

}


