import axios from "axios";
import React from "react";
export default async function Home()
{
    const res = await axios.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=d6a40406acb6477d87c3caa6353d38ed")
    const info = res.data;
    console.log(info);
    return(<>
    <div>
    {info.map((item:any) => (
        
          <li key={item.id}>
          <div>
            {item.author}
          </div>
            </li>
         
        ))}
    
    </div>
    
    </>)
}