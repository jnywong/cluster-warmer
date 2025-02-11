import { FireIcon } from '@heroicons/react/24/outline';

export default function Logo() {
  return (
    <div className={`flex flex-row items-center leading-none text-white`}>
      <strong className="text-[44px]">Cluster Warmer</strong>
      <FireIcon className="h-12 w-12 rotate-[15deg]" />
    </div>
  );
}
