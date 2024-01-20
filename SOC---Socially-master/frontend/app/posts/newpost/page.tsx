'use client'

import axios from "axios"
import CreatePost from "./addpost";
import Header from "@/app/components/header";

export default  function NewBlog()
{
    async function post(postData:any)
    {
        alert("hi");
        console.log(postData);
        const res = await axios.post('http://localhost:8000/newpost/', postData);
        console.log(res.data);
        
        
       


    }

    return <>
    <Header />
    <CreatePost handleSubmit = {post} />
    </>
}
  
