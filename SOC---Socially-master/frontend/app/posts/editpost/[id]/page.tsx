'use client'

import axios from "axios"
import CreatePost from "./post"
import Header from "@/app/components/header";

export default async function EditBlog({params}:{params:any})
{

    const post = await axios.get(`http://localhost:8000/post/${params.id}/`)

    async function patch(postData:any)
    {
        console.log(postData);
       
        try {
            const response = await axios.patch(`http://localhost:8000/post/${params.id}/`, postData);

            console.log('Post created:', response.data);
          } catch (error) {
            console.error('Error creating post:', error);
          }
          window.location.href = "/posts"


    }

    return <>
    <Header />
    <CreatePost handleSubmit={patch} post ={post.data} />
    </>
}