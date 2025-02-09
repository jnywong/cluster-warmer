import Logo from './ui/logo';
import FormComponent from './ui/events/create-form';
import Image from 'next/image';
import { Status } from './ui/status';

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col p-6">
      <div className="flex h-20 shrink-0 items-end rounded-lg bg-orange-500 p-4 2xl:h-52">
        <Logo />
      </div>
      <div className="mt-4 flex grow flex-col gap-4 md:flex-row">
        <div className="flex flex-col justify-center gap-6 rounded-lg bg-gray-50 px-6 py-10">
          <p className={`text-xl text-gray-800 md:text-3xl md:leading-normal`}>
            <strong>Prepare in advance.</strong> Scale up machine resources for your{' '}
            <em className="text-orange-500">JupyterHub</em>, ahead of time.
          </p>
          {/* <Link
            href="/login"
            className="flex items-center gap-5 self-start rounded-lg bg-blue-500 px-6 py-3 text-sm font-medium text-white transition-colors hover:bg-blue-400 md:text-base"
          >
            <span>Log in</span> <ArrowRightIcon className="w-5 md:w-6" />
          </Link> */}
        </div>
        <div className="flex w-full flex-col justify-center gap-6 rounded-lg px-6 py-10">
          <div className="w-full 2xl:w-1/2 px-8 pt-6 pb-8 mb-4">
            <Status />
          </div>
          <div className="w-full 2xl:w-1/2 px-8 pt-6 pb-8 mb-4">
            <FormComponent />
          </div>
        </div>
      </div>
    </main>
  );
}
