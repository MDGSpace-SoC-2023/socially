'use client'

import axios from "axios"
import CreatePost from "./newblog"
import Header from "@/app/components/header";

export default  async function NewBlog()
{
    async function post(postData:any)
    {
       
        try {
            const response = await axios.post('http://localhost:8000/newblog/', postData);

            console.log('Post created:', response.data);
          } catch (error) {
            console.error('Error creating post:', error);
          }
          window.location.href = "/blogpage";


    }

    return <>
    <Header />
    <CreatePost handleSubmit={post} />
    </>
}
  
