import * as React from "react";
import { useForm } from "react-hook-form";
import { Button } from "@/components/ui/button";
import { object, string, InferType } from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import axios from "axios";
import { toast } from "sonner";
import { useNavigate } from "react-router-dom";

const authschema = object({
  email: string().email("Invalid email format.").required("Email is required."),
  password: string().required("Password is required."),
});

type InputType = InferType<typeof authschema>;

const SignIn: React.FC = (): React.ReactElement => {
  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<InputType>({
    resolver: yupResolver(authschema),
  });
  const onSubmit = async (data: InputType) => {
    try {
      const result = await axios.post("http://127.0.0.1:8000/auth/login", data);
      if (result.data.success == true) {
        toast.success(result.data.message);
        navigate("/dashboard");
      }
    } catch (e: unknown) {
      if (axios.isAxiosError(e)) {
        if (e.response) {
          toast.error(e.response.data.message || "Server error");
        } else if (e.request) {
          toast.error("No response from server");
        } else {
          toast.error("Error setting up request");
        }
      } else if (e instanceof Error) {
        toast.error(e.message || "An error occurred");
      } else {
        toast.error("An unknown error occurred");
      }
    }
  };

  return (
    <Card className="w-80 md:w-96">
      <CardHeader>
        <CardTitle>Login</CardTitle>
        <CardDescription>Enter your email and password</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit(onSubmit)}>
          <div className="grid w-full items-center gap-4">
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="name">Email</Label>
              <Input id="name" placeholder="Email" {...register("email")} />
              {errors.email && (
                <Label className="text-destructive">
                  {errors.email?.message}
                </Label>
              )}
            </div>
            <div className="flex flex-col space-y-1.5">
              <Label htmlFor="password">Password</Label>
              <Input
                id="password"
                type="password"
                placeholder="Password"
                {...register("password")}
              />
              {errors.password && (
                <Label className="text-destructive">
                  {errors.password?.message}
                </Label>
              )}
            </div>
            <Button type="submit">SignIn</Button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
};

export default SignIn;
