import { Button } from "./ui/button";
import { DashboardIcon, ReaderIcon, GearIcon } from "@radix-ui/react-icons";

const SideBar = () => {
  return (
    <div className="sticky min-w-max md:p-2 border-r-2 ml-2 rounded-sm">
      <ul className="w-full h-full flex flex-col gap-1">
        <li>
          <Button
            variant="ghost"
            className="flex gap-2 hover:text-primary hover:bg-destructive-foreground"
          >
            <DashboardIcon />
            <span className="hidden md:block lg:block xl:block">Dashboard</span>
          </Button>
        </li>
        <li>
          <Button
            variant="ghost"
            className="flex gap-2 hover:text-primary hover:bg-destructive-foreground"
          >
            <ReaderIcon />
            <span className="hidden md:block lg:block xl:block">Logs</span>
          </Button>
        </li>
        <li>
          <Button
            variant="ghost"
            className="flex gap-2 hover:text-primary hover:bg-destructive-foreground"
          >
            <GearIcon />
            <span className="hidden md:block lg:block xl:block">Settings</span>
          </Button>
        </li>
      </ul>
    </div>
  );
};

export default SideBar;
