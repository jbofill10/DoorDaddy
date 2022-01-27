import './HomeInfo.css'
import * as React from 'react';

type HouseProps = {
	price: string;
	address: string;
}

export const HouseInfo = ({price, address}: HouseProps) => {
	return (
		<div className='HomeInfoWrapper'>
			<div className='Price'>{price}</div>
			<div className='Address'>{address}</div>
		</div>
	)
}