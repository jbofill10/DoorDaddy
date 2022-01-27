import * as React from 'react';
import { HouseInfo } from './components/index';

function App() {
	return (
		<div className='App'>
			<div className='Divider'>
				<div className='HouseDetails'>
					<HouseInfo price='230,500' address='335 Fox Haven Dr Aiken, SC 29803'/>
				</div>
			</div>
		</div>
	)
}

export default App;