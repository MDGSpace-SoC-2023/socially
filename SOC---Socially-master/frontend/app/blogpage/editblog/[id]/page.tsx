'use client'

import axios from "axios"
import CreatePost from "./blog"
import Header from "@/app/components/header";

export default  async function NewBlog({params}:{params:any})
{

    const blog = await axios.get(`http://localhost:8000/blog/${params.id}/`)

    async function post(postData:any)
    {
       
        try {
            const response = await axios.patch(`http://localhost:8000/blog/${params.id}/`, postData);

            console.log('Post created:', response.data);
          } catch (error) {
            console.error('Error creating post:', error);
          }
          window.location.href = "/blogpage"


    }

    return <>
    <Header />
    <CreatePost handleSubmit={post} blog ={blog.data} />
    </>
}