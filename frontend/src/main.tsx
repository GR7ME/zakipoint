import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, Navigate, RouterProvider } from "react-router-dom";
import "./index.css";
import SignUp from "@/pages/login/SignUp.tsx";
import SignIn from "@/pages/login/SignIn.tsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/login"/>,
  },
  {
    path: "/login/",
    element: <SignIn />
  },
  {
    path: "signup/",
    element: <SignUp />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
