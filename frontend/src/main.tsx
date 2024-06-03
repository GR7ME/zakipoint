import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from "./App.tsx";
import "./index.css";
import SignUp from "@/pages/login/SignUp.tsx";
import SignIn from "@/pages/login/SignIn.tsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/login/",
    children: [
      {
        path: "signup/",
        element: <SignUp />,
      },
      {
        path: "signin/",
        element: <SignIn />,
      },
    ],
  }
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
