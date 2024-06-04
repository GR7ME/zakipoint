import zph from "@/assets/zph.webp";
import {
  QuestionMarkCircledIcon,
  BellIcon,
  AvatarIcon,
} from "@radix-ui/react-icons";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

const loggroups: string[] = ["pyspark-1", "pyspark-2"];

const NavBar = () => {
  return (
    <div className="flex justify-between items-center mx-2 my-2 border border-b-2">
      <div className="w-36 flex">
        <img src={zph} />
        <div className="">
          <Select>
            <SelectTrigger className="w-28 border-0 font-light">
              <SelectValue placeholder="log-group" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup className="text-sm font-light">
                <SelectLabel>Log Groups</SelectLabel>
                {loggroups.map((value) => (
                  <SelectItem key={value} value={value}>
                    {value}
                  </SelectItem>
                ))}
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
      </div>
      <div className="p-1 flex gap-4 mr-2">
        <div>
          <QuestionMarkCircledIcon />
        </div>
        <div>
          <BellIcon />
        </div>
        <div>
          <AvatarIcon />
        </div>
      </div>
    </div>
  );
};

export default NavBar;
