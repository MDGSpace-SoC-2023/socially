'use client'
import { UserButton, useUser } from "@clerk/nextjs";
import Link from "next/link";
import React from "react";
export default function Nav()

{
    const {user,isLoaded} = useUser();
    return(
        <header>

            <nav>

                <div><a href="/">NextJs Authentication</a></div>
                {
                    isLoaded && user && (
                    <>

                    <Link  href="/"> Dashboard </Link>
                    <UserButton afterSignOutUrl="/"/>
                    </>)
                }
                
            </nav>

        </header>
    )
}