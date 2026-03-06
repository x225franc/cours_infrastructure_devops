import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { useCustomDate } from "./app/composables/useCustomDate";

describe("Composable useCustomDate", () => {
    beforeEach(() => {
        vi.useFakeTimers();
        // Simuler la date actuelle au 10-01-2024
        vi.setSystemTime(new Date("2024-01-10"));
    });

    afterEach(() => {
        vi.useRealTimers();
    });

    it("devrait calculer twoDaysAgo correctement", () => {
        const { twoDaysAgo } = useCustomDate();
        const expected = new Date("2024-01-08");
        expect(twoDaysAgo.value).toEqual(expected);
    });

    it("devrait calculer lastYear correctement", () => {
        const { lastYear } = useCustomDate();
        const expected = new Date("2023-01-10");
        expect(lastYear.value).toEqual(expected);
    });

    it("devrait retourner absoluteMinDataDate comme 1er janvier 1946", () => {
        const { absoluteMinDataDate } = useCustomDate();
        const expected = new Date(1946, 0, 1);
        expect(absoluteMinDataDate.value).toEqual(expected);
    });
});
