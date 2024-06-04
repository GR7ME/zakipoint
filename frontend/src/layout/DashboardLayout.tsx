import NavBar from "@/components/NavBar";
import Sidebar from "@/components/SideBar";
import { Outlet } from "react-router-dom";

export const DashboardLayout = () => {
  return (
    <>
      <NavBar />
      <div className="flex w-full h-full mb-2 gap-2">
        <Sidebar />
        <div className="border-2 mr-2 w-full p-2 rounded-sm flex justify-center items-center">
        <Outlet />
        </div>
      </div>
    </>
  );
};

export default DashboardLayout;
