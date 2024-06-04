import { Button } from "./ui/button";
import { DashboardIcon, ReaderIcon, GearIcon } from "@radix-ui/react-icons";

const SideBar = () => {
  return (
    <div className="sticky min-w-max p-4 border-dashed border-r-2">
      <ul className="w-full h-full flex flex-col mx-2 gap-1">
        <li>
          <Button
            variant="ghost"
            className="flex gap-2 hover:text-destructive hover:bg-destructive-foreground"
          >
            <DashboardIcon />
            Dashboard
          </Button>
        </li>
        <li>
          <Button
            variant="ghost"
            className="flex gap-2 hover:text-destructive hover:bg-destructive-foreground"
          >
            <ReaderIcon />
            Logs
          </Button>
        </li>
        <li>
          <Button
            variant="ghost"
            className="flex gap-2 hover:text-destructive hover:bg-destructive-foreground"
          >
            <GearIcon />
            Settings
          </Button>
        </li>
      </ul>
    </div>
  );
};

export default SideBar;
