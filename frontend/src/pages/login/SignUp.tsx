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

const authschema = object({
  email: string()
    .email("Invalid email format.")
    .required("Email is required."),
  password: string()
    .required("Password is required.")
    .min(8, "Password must be at least 8 characters long.")
    .max(20, "Password cannot be more than 20 characters long.")
})


type InputType = InferType<typeof authschema>;

const SignUp: React.FC = (): React.ReactElement => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<InputType>({
    resolver: yupResolver(authschema),
  });
  const onSubmit = (data) => console.log(data);

  console.log(watch("email"));

  return (
    <Card className="w-80 md:w-96">
      <CardHeader>
        <CardTitle>Create an account</CardTitle>
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
              <Input id="password" type="password" placeholder="Password" {...register("password")} />
              {errors.password && (
                <Label className="text-destructive">
                  {errors.password?.message}
                </Label>
              )}
            </div>
            <Button type="submit">SignUp</Button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
};

export default SignUp;
