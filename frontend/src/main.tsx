import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, Navigate, RouterProvider } from "react-router-dom";
import "./index.css";
import SignUp from "@/pages/login/SignUp.tsx";
import SignIn from "@/pages/login/SignIn.tsx";
import LoginLayout from "./layout/LoginLayout";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/auth/login"/>,
  },
  {
    path: "/auth",
    element: <LoginLayout/>,
    children: [
      {
        path: "login/",
        element: <SignIn/>
      },
      {
        path: "signup/",
        element: <SignUp />,
      },
    ]
  }
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
