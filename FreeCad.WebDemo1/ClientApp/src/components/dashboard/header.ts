import { Component, Vue } from 'vue-property-decorator';
import { TopnavbarEvents } from 'common/eventbus';

@Component
export default class HeaderComponent extends Vue {

    // Used for larger non-mobile screens
    private toggle_leftsidemenu_click(event: Event) {
        TopnavbarEvents.$emit('toggle-leftsidemenu');
    }

}
