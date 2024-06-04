import { Outlet } from "react-router-dom";
import zph from "../assets/zph.webp"

const LoginLayout = ()=>{
    return <>
    <div className="w-[100%] h-[100%] flex flex-col gap-4 justify-center items-center">
    <img src={zph} className="h-24"></img>
    <Outlet/>
    </div>
    </>
}

export default LoginLayout;