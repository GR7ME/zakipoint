import "./App.css";
// import React from "react";
// import ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  Navigate,
  RouterProvider,
} from "react-router-dom";
import "./index.css";
import SignUp from "@/pages/login/SignUp.tsx";
import SignIn from "@/pages/login/SignIn.tsx";
import LoginLayout from "./layout/LoginLayout";
import DashboardLayout from "@/layout/DashboardLayout";
import { Toaster } from "@/components/ui/sonner"

const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/auth/login" />,
  },
  {
    path: "/auth",
    element: <LoginLayout />,
    children: [
      {
        path: "login/",
        element: <SignIn />,
      },
      {
        path: "signup/",
        element: <SignUp />,
      },
    ],
  },
  {
    path: "/dashboard",
    element: <DashboardLayout />,
    children: [
      {
        index: true,
        element: <p>Dashboard page</p>,
      },
      {
        path: "logs/",
        element: <p>logs page</p>,
      },
      {
        path: "settings/",
        element: <p>settings page</p>,
      },
    ],
  },
]);

function App() {
  return (
    <>
    <RouterProvider router={router} />
    <Toaster richColors position="top-right" />
    </>
  );
}

export default App;
